import pygame
import pygame_menu
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from Constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class HighScoreMenu():
    def __init__(self,close_function):
        self.close_function = close_function
        self.high_scores_data = HighScoresData()
    """Class for accessing and displaying all previous high scores"""
    def retrieve_high_scores(self):
        
        self.high_score_list = self.high_scores_data.display_top_ten()

    def show_high_scores(self):
        self.high_score_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.high_score_screen = pygame_menu.Menu("Highscores",SCREEN_WIDTH,SCREEN_HEIGHT,onclose=self.close)
        self.high_score_screen.add.label("Highscores:")


        self.retrieve_high_scores()
        for i in range(1,11):
            new_score_user = self.high_score_list.get(i)[0]
            new_score = self.high_score_list.get(i)[1]
            self.high_score_screen.add.label(f"{i} {new_score_user} ---------------------- {new_score}" + " " * 45) 
        
        self.high_score_screen.add.button("Back",self.close)
        self.high_score_screen.mainloop(self.high_score_surface)
    
    def get_top_score(self):
        return self.high_scores_data.top_ten_ref.child("1").get().get("score")
               

    def close(self):
        self.close_function()




class HighScoresData():
    """Class to handle working with the Particle Builder high scores database"""
    def __init__(self):
        cred = credentials.Certificate("main_menu/particle_builder_authentication_key.json")
        try:
            firebase_admin.initialize_app(cred, {
                "databaseURL":"https://particle-builder-default-rtdb.firebaseio.com/"
            })
        except:
            pass

        self.top_ten_ref = db.reference("top_ten")
        self.top_100_ref = db.reference("top_hundred")

    def rearrange_top_ten(self,starting_place,new_score,new_user):
        """Function to place a new score into the top 10 list, and rearranging the scores below that new number"""
        #10th place will have to go to the rest of the list, regardless of which place is being changed
        tenth_place_score = self.top_ten_ref.child("10").get().get("score")
        tenth_place_user = self.top_ten_ref.child("10").get().get("user")
        
        self.rearrange_top_hundred(11,tenth_place_score,tenth_place_user)

        if starting_place == 10:
            self.top_ten_ref.child("10").update({
                "score": new_score,
                "user": new_user
            })
        
        else:
            for i in range(starting_place,11):
                current_place_score = self.top_ten_ref.child(str(i)).get().get("score")
                current_place_user = self.top_ten_ref.child(str(i)).get().get("user")

                self.top_ten_ref.child(str(i)).update({
                    "score":new_score,
                    "user":new_user
                })
                self.top_100_ref.child(str(i)).update({
                    "score": new_score,
                    "user": new_user
                })

                new_score = current_place_score
                new_user = current_place_user

    def rearrange_top_hundred(self,starting_place,new_score,new_user):
        """Function to place a new score into the top 100 list, and rearranging the scores below that new number"""
        if starting_place == 100:
            self.top_100_ref.child("100").update({
                "score": new_score,
                "user": new_user
            })
            
        else:
            for i in range(starting_place,101):
                current_place_score = self.top_100_ref.child(str(i)).get().get("score")
                current_place_user = self.top_100_ref.child(str(i)).get().get("user")

                self.top_100_ref.child(str(i)).update({
                    "score": new_score,
                    "user": new_user
                })
                new_score = current_place_score
                new_user = current_place_user

    def update_top_ten(self,new_score,new_user):
        """Function to check if a new score belongs on the top 10 list. 
        If it does, this function places that score in the list"""
        in_top_ten = False
        for i in range(1,11):
            current_score_to_compare = float(self.top_ten_ref.child(str(i)).get().get("score"))
            if new_score > current_score_to_compare:
                print(f"This score should be in {i} place")
                self.rearrange_top_ten(i,str(new_score),new_user)
                in_top_ten = True
                break
                
        if not in_top_ten:
            print("That score didn't make it")
            self.update_top_100(new_score,new_user)

    def update_top_100(self,new_score,new_user):
        """Function to check if a new score belongs on the top 100 list. 
        If it does, this function places that score in the list.z"""
        bottom_score = self.top_100_ref.child("100").get().get("score")
        if new_score > float(bottom_score):
            in_top_100 = False
            for i in range(11,101):
                current_score_to_compare = float(self.top_100_ref.child(str(i)).get().get("score"))
                if new_score > current_score_to_compare:
                    self.rearrange_top_hundred(i,new_score,new_user)
                    

    def display_top_ten(self):
        """Function to retreive the top 10 list for displaying"""
        display_dict = {}
        for i in range(1,11):
            score = self.top_ten_ref.child(str(i)).get().get("score")
            user = self.top_ten_ref.child(str(i)).get().get("user")
            display_dict[i] = [user,score]
            
        return display_dict

    def display_top_hundred(self):
        """Function to retreive the top 100 list for displaying"""
        display_dict = {}
        for i in range(1,101):
            score = self.top_100_ref.child(str(i)).get().get("score")
            user = self.top_100_ref.child(str(i)).get().get("user")
            display_dict[i] = [user,score]

        return display_dict

    def clear_top_ten(self):
        """Function to clear the top 10 list's data from the database"""
        for i in range(1,11):
            self.top_ten_ref.child(str(i)).update({
                "score":"0",
                "user":" "
            })

    def clear_top_hundred(self):
        """Function to clear the top 100 list's data from the database"""
        for i in range(1,101):
            self.top_100_ref.child(str(i)).update({
                "score": "0",
                "user": " "
            })

    def clear_all(self):
        """Function to clear the entire database, both top 10 and 100 lists"""
        for i in range(1,101):
            if i < 11:
                self.top_ten_ref.child(str(i)).update({
                    "score": "0",
                    "user": " "
                })

            self.top_100_ref.child(str(i)).update({
                "score": "0",
                "user": " "
            })