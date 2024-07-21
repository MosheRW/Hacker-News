from matplotlib import pyplot as plt
from item import Item
import api, os, datetime, csv, tqdm


def resize_for_Dbug(array:list, new_size:int = 10) -> list:
    new_arr = []
    
    for i in tqdm.tqdm(range(new_size)):
        new_arr.append(array[i])
        
    return new_arr




def repurpose_the_array(uids_list:list) ->  None:
    """
        name:  repurpose_the_array
        
        input:  array contains items uids
        output: None. but changes the inserted list
        
        part:   convert the int types uids, to the item objects of the samr uids
        """
        
    for i, uid in tqdm.tqdm(enumerate(uids_list)):  
        uids_list[i] = Item(api.get_item(uid))
        

def constract_comments_array(stories_list:list)    ->  list:
    """
        name:   constract_comments_array
        
        input:  the stories list array
        output: array that contains all the top comments uids
        
        part:   travers on the previous array and haverst the the comments uid's and place them in an array
        """
        
    comments_uids = []
    
    for story in tqdm.tqdm(stories_list):
        prev_len = len(comments_uids)
        comments_uids += story.comments
        
        for i in tqdm.tqdm(range(len(story.comments))):
            story.extend_coments(i, i + prev_len)

    return  comments_uids


def statistics()    -> list:
    #   TODO:    needs to decide if the list wil be a tupls list 
    """
        name:  statistics
        
        input:  None, but uses the two global arrays            
        output: list of the statistics data
        
        part:   calculate the statistics, and return list of them (maybe as tupls)
        """
    #   TODO:   statistics script
    stats = [stats_dict_2_sorted_list_tuples(   
                                how_many_pulished_at_any_date(top_stories))]
    stats = [stats_dict_2_sorted_list_tuples(
                                how_many_pulished_at_any_date(comments))]
    

    stats += [stats_dict_2_sorted_list_tuples(
                                how_many_pulished_at_any_weekDay(top_stories))]
    stats += [stats_dict_2_sorted_list_tuples(
                                how_many_pulished_at_any_weekDay(comments))]
    

    stats += [stats_dict_2_sorted_list_tuples(
                                how_many_pulished_comapaird_to_the_weekDay(top_stories))]
    stats += [stats_dict_2_sorted_list_tuples(
                                how_many_pulished_comapaird_to_the_weekDay(comments))]
    

    return stats


def stats_dict_2_sorted_list_tuples(pack:dict)    -> list:
   
    unpack = list(zip(pack.keys(), pack.values()))
    
    unpack.sort()
    
    return unpack

def extract_the_ith_arg(arr:list, i:int = 0) -> list:
    
    return [arg[i] for arg in arr]


def how_many_pulished_at_any_date(arr:list)    ->  dict:
    """
        name:  how_many_stories_pulished_at_any_date
        
        input:  None.
        output: dict with num of publications for any day in the last 500 publications  
        """
    dates = {}      #   {date :     counter}
    for story in arr:
       
        date = datetime.datetime.fromtimestamp(story.time_of_creation)
        
        date = str(date.month)  +   str(date.day)
        
        dates[date] = dates.get(date, 0) + 1
        


    return dates

def how_many_pulished_at_any_weekDay(arr:list)    ->  dict:
    """
        name:  how_many_stories_pulished_at_any_weekDay
        
        input:  None.
        output: dict with num of publications for any weekDay in the last 500 publications  
        """
    dates = {}      #   {date :     counter}
    for story in arr:
       
        date = datetime.datetime.fromtimestamp(story.time_of_creation)

        dates[date.weekday()] = dates.get(date.weekday(), 0) + 1
        
    return dates
    
def how_many_pulished_comapaird_to_the_weekDay(arr:list)    ->  dict:
    """
        name:  how_many_coments_comapaird_to_the_week_day
        
        input:  None.
        output: dict with num of publications for any weekDay in the last 500 publications  
        """
    dates = {}      #   {date :     counter}
    for story in arr:
       
        date = datetime.datetime.fromtimestamp(story.time_of_creation)

        dates[date.weekday()] = dates.get(date.weekday(), 0) + len(story)
        
    return dates
 
#TODO:  need to fix the zero day
#TODO:  need to add title to the window
    
def statistics_table() -> list:
    stats = []
    
    stats.append("num of pulished storirs: ", len(top_stories))
    stats.append("num of pulished comments: ", len(comments))
    stats.append("average number of stories a day: ",   
                 len(top_stories)  /   len(how_many_pulished_at_any_date(top_stories)) )
    stats.append("average number of comments a day: ",   
                 len(top_stories)  /   len(how_many_pulished_at_any_date(comments)) )
    

    
#   TODO:   Auxiliary functions for statistics

def save_as_CSV(array:list, headers_array:list, file_name:str)   ->  None:       
    """
        name:  item.extend_coments
        
        input:  
            -   list of row dictionaries
            -   list of the csv headers
            -   file name
            -   folder path
        output: None.   but careat new CSV file with the data in it
        
        part:   save the data as csv file
        """

    print(os.getcwd())
    with open(file_name + ".csv", 'w',  encoding="utf-8") as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=headers_array)
 
        # writing headers (field names)
        writer.writeheader()
 
        # writing data rows
        writer.writerows(array)

def show_statistics(stats:list)   -> None:
    #   TODO:    show_statistics documantation 
    """
        name:  show_statistics
        
        input:  None.           
        output: None.
        
        part:  
        """
    #   TODO:   show_statistics script
    
    for stat in stats:
    
      #  plt.plot(extract_the_ith_arg(stat,0), extract_the_ith_arg(stat,1))
        plt.plot(extract_the_ith_arg(stat,1), extract_the_ith_arg(stat,0))
        plt.show()

    



#	Harvest the top stories uid's and place them in an array
top_stories = api.get_top_stories()
top_stories = resize_for_Dbug(top_stories, 10)

#	creat objects to every uid story and place it in the OG array. function
repurpose_the_array(top_stories)

#	travers on the previous array and haverst the the comments uid's and place them in an array
comments = constract_comments_array(top_stories)

#	creat objects to every uid story and place it in the OG array. function
repurpose_the_array(comments)


#	statistics:
stats_graph    =   statistics()
#stats_table    =   statistics_table()



#   -----------         CSV's files         ----------

#   the folder name for the files we'll save that time
folder_name = datetime.datetime.now().strftime("%m_%d_%H_%M_%S")


#   changing the location for save the file in the right place
if not os.path.exists("files"):
    os.mkdir("files")
print(os.getcwd())
os.chdir("files") 
os.mkdir(folder_name)
os.chdir(folder_name) 

#   the headers for the stories and comments csv tables 
items_headers = ["uid", "title", "the content", "writer", "Published at", "score", "comments_quantity"]

#	create and save the stories CSV file
save_as_CSV(    [item.get_as_dict() for item in top_stories],    items_headers, "top_stories")

#	create and save the comments CSV file
save_as_CSV(    [item.get_as_dict() for item in comments],    items_headers, "comments")

#	create and save the statistics CSV file
#save_as_CSV(    stats,    items_headers,  "stats")     #	TODO:	the stories statistics file		<-


 #   -----------         visualization         ----------

#	show the statistics on the screen
show_statistics(stats_graph)




print("THE END")