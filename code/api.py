"""
    module, that providing api functions to the Hacker News website
    """


import urllib3


address_prefix = 'https://hacker-news.firebaseio.com/v0/'
address_suffix = '.json'

second_prefix = {"item" : "item/", 
                 "user" : "user/",
                 "index" : ""}


def get(header:int | str, classify:str = "item") -> dict | list: 
    
    if classify == "item":
        address = address_prefix + second_prefix[classify] + str(header) + address_suffix
    else:
        address = address_prefix + second_prefix[classify] + header + address_suffix
    
    return urllib3.request("GET",address).json()
      

def get_item(id: int) -> dict:
    return get(id, "item")

def get_top_stories() -> list:
    return get("topstories", "index")

def get_new_stories() -> list:
     return get("newstories", "index")
 
def get_best_stories() -> list:
     return get("beststories", "index")
 
def get_ask_stories() -> list:
     return get("askstories", "index")
  
def get_show_stories() -> list:
     return get("showstories", "index")
  
def get_job_stories() -> list:
     return get("jobstories", "index")
  
def get_max_item()  -> int:
     return get("maxitem", "index")

