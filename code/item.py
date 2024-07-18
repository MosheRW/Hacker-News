

class Item:
    #   TODO:   documantation
    """
    name:   Item
    perpuse:    to store hackerNews stories and comments in an orgenized methode
    main functions:
        -   item.extend_coments: get two indicators, 
        and place the second one in a tuple alongside with the comment indexed with the first iserted index
        -   item.get_as_dict: retruns dictionary with the important attributes in a way thats suits CSV files
    
    attributes:
        -   __url: The URL of the story.
        -   __uid: The item's unique id.
        -   __writer: The username of the item's author
        -   __time_of_creation: Creation date of the item, in Unix Time.
        -   __score: The story's score.
        -   __comments_quantity:  The total comment count
        -   __title: The title of the story.
        -   __the_content: The total comment count.
        -   __comments: The comments, in ranked display order.
    
    """
    
    def __init__(self, argumants: dict) -> None:
        """
        name:   item.__init__
        input:  argumants dictionary
        output: item object, nothing.
        
        part:   to creat and initlize an item object
        """
        
        #Details
        self.__url = argumants.get("url","")                       #   The URL of the story.
        self.__uid = argumants.get("id","")                        #   The item's unique id.
        self.__writer = argumants.get("by","")                     #   The username of the item's author.
        self.__time_of_creation = argumants.get("time","")         #   Creation date of the item, in Unix Time.
        
        #Statistics
        self.__score = argumants.get("score","")                   #   The story's score.
        self.__comments_quantity = argumants.get("descendants","") #   The total comment count.

        #The real content
        self.__title = argumants.get("title","")                   #   The title of the story.
        self.__the_content = argumants.get("text","")              #   The comment or story text.
        
        """
        initilize with The ids of the item's comments, in ranked display order.
        But during the program we well replace them with tuples,
        whom conatains in adddition to the id, the index of the comment in the other  array     """
        self.__comments = argumants.get("kids","")                  #   The ids of the item's comments, in ranked display order.
                                                          
    
#   ---------   class getters     ---------
    @property
    def url(self) -> str:
        return  self.__url
        
    @property
    def uid(self) -> int:
        return self.__uid

    @property
    def writer(self) -> str:
        return self.__writer
        
    @property
    def time_of_creation(self) -> int:
        return self.__time_of_creation
        
    @property
    def score(self) -> int:
        return self.__score
        
    @property   
    def comments_quantity(self) -> int:
        return self.__comments_quantity

    @property
    def comments(self) -> list:
        return self.__comments

#   ---------   class special set methodes     ---------

    def   extend_coments(self, inner_index:int , outer_index:int)  -> None:
        """
        name:  item.extend_coments
        
        input:  
            -   the internal index of the comment.
            -   the new outer index of the comment.                
        output: None.
        
        part:   to add the outer index of the full detailed comment in the second array
        """
        self.__comments[inner_index] = (outer_index, self.__comments[inner_index])
        
    

#   ---------   class special get methodes     ---------    

    #   get methode that returns the title, text, and statistics as str
    def get_as_str(self, separator:str = "\n")    ->  str:
        """
        name:  item.get_as_str
        
        input:  separator (opt, default is 'endl')
        output: the title, text, and statistics as str
        
        part:   get methode that returns the title, text, and statistics as str
        """
        return "{ " + self.__title + separator + self.__the_content + separator    +\
                     "score: "  +   str(self.__score)    +   separator  +\
                 "comments_quantity: "   +   str(self.__comments_quantity) + " }"
    

    #   get methode that return all the data, in a stracture that suits to CSV
    def get_as_dict(self)    ->  dict:
        """
        name:  item.get_as_dict
        
        input:  None.
        output: dictionary with all the data except the comments uids
        
        part:   get methode that return all the data, in a stracture that suits to write a CSV.
        """
        out = { "uid"               :   self.__uid,
                "title"             :   self.__title,
                "the content"       :   self.__the_content,
                "writer"            :   self.__writer,
                "Published at"      :   self.__time_of_creation,
                "score"             :   self.__score,
                "comments_quantity" :   self.__comments_quantity    }
        
        return out

    
#   ---------   class representation methodes     ---------

    def __repr__(self) -> str:
        return self.get_as_str(", ")
    
    #   str
    def __str__(self) -> str:

        out =   "{ "                                                        +   \
                "uid: "                 +   str(self.__uid)                 +   \
                "title: "               +   self.__title                    +   \
                "the content: "         +   self.__the_content              +   \
                "writer: "              +   self.__writer                   +   \
                "Published at: "        +   str(self.__time_of_creation)    +   \
                "score: "               +   str(self.__score)               +   \
                "comments_quantity: "   +   str(self.__comments_quantity)   +   " }"  
        
        return out
    
#   TODO: erease thos sections if the will not be use
    
#   ---------   class special copmarison methodes   ---------    


#   ---------   class copmarison methodes           ---------    


#   ---------   class special methodes              ---------    

    def __len__(self)   -> int:
        assert self.__comments_quantity == len(self.__comments), "Error!"        
        #return self.__comments_quantity
        return len(self.__comments)

    