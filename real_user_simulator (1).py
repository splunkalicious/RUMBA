########################################################################################
##  Real User Simulator

from nav_matrix import nav_matrix
from user_agents import user_agents
import asyncio
from pyppeteer import launch
import re
import random
import time
# from time import sleep

def frothly_page(url):
    return re.search("https:\/\/frothly\.notsplunktshirtco\.com(\/[^\/]*)", url).group(1)



def frothly_sub_page(url):
    sub_page = re.search("https:\/\/frothly\.notsplunktshirtco\.com\/[^\/]+(\/[^\/]*)", url)
    if sub_page is None:
        return("")
    else:
        return(sub_page.group(1))

    
    
def get_selector(url):
    selector_list = nav_matrix[frothly_page(url)]
    
    random_index= random.randint(0,100)
    
    for selector in selector_list:
        if random_index > selector[0]:
            break
    return(selector[1])



async def sim_user(site, run_number):
    #print("testing " + site + " link number:" + str(link_number))
    
    # Set options for chromium browser and open
    loptions = {"headless": True,
                'args': ['--no-sandbox']
        
    }
    browser = await launch(options=loptions)
    page = await browser.newPage()
    await page.setUserAgent(random.choice(user_agents))
    
    options = {"waitUntil": 'load',
               "timeout": 1000000}
    await page.goto(site, options=options)
    
    #print("Browser launched")
    # get link button
    
    step_counter = 1
    #browsing loop
    while True:
        
        await asyncio.sleep(10) # update this to be dependent on page content for realism
        # await page.screenshot({'path': "simulated_user_number_" + str(run_number) + "_step_" + str(step_counter) + '.png'})
        current_url = await page.evaluate("() => window.location.href")
        print("Session:" + str(run_number) + " step:" + str(step_counter) + " " + current_url)
        step_counter +=1
        if frothly_sub_page(current_url)=="/checkout":
            break
        selector = get_selector(current_url)
        #print(selector)

        await page.waitForSelector(selector)
        await page.click(selector) 
    await browser.close()
       
        

#Set Maximum number of parralel sessions to run
active_task_limit = 40

async def main_loop():
    session_count =0
    session_start = time.time()
    while True:

        if len(asyncio.all_tasks())<=active_task_limit:
            try:
                    co_routine = sim_user("https://frothly.notsplunktshirtco.com/", session_count)
                    task = asyncio.create_task(co_routine)
                    await asyncio.sleep(0.1)
            except:
                pass
            session_count +=1
        else:
            print("Over " + str(active_task_limit) + " sessions currently running, pausing session creation")
           
        # wait between 5 and 20 sseconds before attempting to start a new session
        wait_time = random.randint(5,20)
        await asyncio.sleep(wait_time)
        
        # Suspend runtime after 30 mins to avoid resource exhaustion
        if (time.time() - session_start) > (30*60):
            print("Script has run for over 30 minutes")
            break
        
asyncio.run(main_loop())