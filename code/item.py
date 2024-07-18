

class item:
    """
    name:
    perpuse:
    main functions:
    
    attributes:
    """
    
    def __init__(self, argumants: dict) -> None:
        """
        name:   item.__init__
        input:  argumants dictionary
        output: item object, nothing.
        
        part:   to creat and initlize an item object
        """
        
        #Details
        self.__url = argumants["url"]                       #   The URL of the story.
        self.__uid = argumants["id"]                        #   he item's unique id.
        self.__writer = argumants["by"]                     #   The username of the item's author.
        self.__time_of_creation = argumants["time"]         #   Creation date of the item, in Unix Time.
        
        #Statistics
        self.__score = argumants["score"]                   #   The story's score.
        self.__comments_quantity = argumants["descendants"] #   The total comment count.

        #The real content
        self.__title = argumants["title"]                   #   The title of the story.
        self.__the_content = argumants["text"]              #   The comment or story text.
        
        """
        initilize with The ids of the item's comments, in ranked display order.
        But during the program we well replace them with tuples,
        whom conatains in adddition to the id, the index of the comment in the other  array     """
        self.__comments = []                                #   The ids of the item's comments, in ranked display order.
                                                          
    
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

    def   extend_coments(self, inner_index:int , comment_uid:int, outer_index:int)  -> None:
        """
        name:  item.extend_coments
        
        input:  
            -   the internal index of the comment.
            -   the  comment uid.
            -   the new outer index of the comment.                
        output: None.
        
        part:   to add the outer index of the full detailed comment in the second array
        """
        pass
        
    

#   ---------   class special get methodes     ---------    

    #   get methode that returns the title, text, and statistics as str
    def get_as_str(self)    ->  str:
        """
        name:  item.get_as_str
        
        input:  None.
        output: the title, text, and statistics as str
        
        part:   get methode that returns the title, text, and statistics as str
        """
        pass
    
    #   get methode that return all the data, in a stracture that suits to CSV
    def get_as_dict(self)    ->  dict:
        """
        name:  item.get_as_dict
        
        input:  None.
        output: dictionary with all the data except the comments uids
        
        part:   get methode that return all the data, in a stracture that suits to write a CSV.
        """
        pass
    
    
#   ---------   class special representation methodes     ---------

    #   repr
    
    #   str
    
    
#   ---------   class special copmarison methodes     ---------    