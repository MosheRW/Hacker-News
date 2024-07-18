from item import Item
import api, os, datetime


def resize_for_Dbug(array:list, new_size:int = 10) -> list:
    new_arr = []
    
    for i in range(new_size):
        new_arr.append(array[i])
        
    return new_arr




def repurpose_the_array(uids_list:list) ->  None:
    """
        name:  repurpose_the_array
        
        input:  array contains items uids
        output: None. but changes the inserted list
        
        part:   convert the int types uids, to the item objects of the samr uids
        """
        
    for i, uid in enumerate(uids_list):  
        uids_list[i] = Item(api.get_item(uid))

def constract_comments_array(stories_list:list)    ->  list:
    """
        name:   constract_comments_array
        
        input:  the stories list array
        output: array that contains all the top comments uids
        
        part:   travers on the previous array and haverst the the comments uid's and place them in an array
        """
    comments_uids = []
    
    for story in stories_list:
        prev_len = len(comments_uids)
        comments_uids += story.comments
        
        for i in range(len(story.comments)):
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
    pass

#   TODO:   Auxiliary functions for statistics

def save_as_CSV(array:list, headers_array:list, file_name:str, folder_path:str)   ->  None:       
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
    #   TODO:   save_as_CSV script
    pass    

def show_statistics()   -> None:
    #   TODO:    show_statistics documantation 
    """
        name:  item.extend_coments
        
        input:  
            -   the internal index of the comment.
            -   the  comment uid.
            -   the new outer index of the comment.                
        output: None.
        
        part:   to add the outer index of the full detailed comment in the second array
        """
    #   TODO:   show_statistics script
    pass



#	Harvest the top stories uid's and place them in an array
top_stories = api.get_top_stories()
top_stories = resize_for_Dbug(top_stories)

print("top_stories: ", top_stories)
#	creat objects to every uid story and place it in the OG array. function
repurpose_the_array(top_stories)
print("top_stories: ", top_stories)

#	travers on the previous array and haverst the the comments uid's and place them in an array
#	TODO:	travers on the previous array and haverst the the comments uid's and place them in an array		<-
comments = constract_comments_array(top_stories)
print("comments: ", comments)
#	creat objects to every uid story and place it in the OG array. function
repurpose_the_array(comments)
print("comments: ", comments)

#	TODO:	find out what are the top-level comments, and how to get them									<-

#	statistics:
#	TODO:	which statistics				<-
#	TODO:	which order						<-
#	TODO:	how								<-
stats = statistics()



#	CSV's files
items_headers = ["uid", "title", "the content", "writer", "Published at", "score", "comments_quantity"]

folder_name = datetime.datetime.now().strftime("%m_%d_%H_%M_%S")

#	the stories CSV file
save_as_CSV(    top_stories,    items_headers,  "top_stories",
            os.getcwd() + "\\files\\" + folder_name + "\\")

#	the comments CSV file
save_as_CSV(    comments,    items_headers,  "top_comments",
            os.getcwd() + "\\files\\" + folder_name + "\\")

#	the statistics CSV file
save_as_CSV(    comments,    items_headers,  "top_comments",
            os.getcwd() + "\\files\\" + folder_name + "\\")         #	TODO:	the stories statistics file		<-

#	show the statistics on the screen
show_statistics()




print("THE END")