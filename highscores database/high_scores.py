import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class HighScores():
    """Class to handle working with the Particle Builder high scores database"""
    def __init__(self):
        cred = credentials.Certificate("particle_builder_authentication_key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL":"https://particle-builder-default-rtdb.firebaseio.com/"
        })

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