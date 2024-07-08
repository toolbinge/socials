import firebase_admin
from firebase_admin import credentials, db

# Path to your service account key file
cred = credentials.Certificate(
    "C:/Users/thaaa/Desktop/socials/toolbinge-log-firebase-adminsdk-ol9rx-3d911b209f.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://toolbinge-log-default-rtdb.firebaseio.com/"}
)


def setup_structure():
    ref = db.reference("/")

    questions = {
        "What_type_of_content_makes_you_cum_the_hardest": {
            "Public_fun": 0,
            "Throat_fuck": 0,
            "Bareback": 0,
            "Cumshots": 0,
        },
        "What_kind_of_public_fun_turns_you_on_the_most": {
            "Nature": 0,
            "Crowds": 0,
            "Public_transport": 0,
            "Beaches": 0,
        },
        "What_aspect_of_throat_fucking_excites_you": {
            "Gagging_sounds": 0,
            "Deepthroat": 0,
            "Face_fucking": 0,
            "Throat_bulge": 0,
        },
        "What's_your_favorite_part_of_bareback_action": {
            "Raw_feeling": 0,
            "Creampies": 0,
            "Breeding": 0,
            "Seed_swapping": 0,
        },
        "Where_do_you_prefer_to_see_cumshots": {
            "Face": 0,
            "Chest": 0,
            "Ass": 0,
            "Mouth": 0,
        },
        "What_natural_setting_gets_you_most_excited": {
            "Forests": 0,
            "Mountains": 0,
            "Rivers_Lakes": 0,
            "Fields": 0,
        },
        "What_crowded_place_turns_you_on_the_most": {
            "Clubs": 0,
            "Beaches": 0,
            "Parks": 0,
            "Sporting_events": 0,
        },
        "Which_form_of_public_transport_excites_you_most": {
            "Bus": 0,
            "Train": 0,
            "Subway": 0,
            "Airplane": 0,
        },
        "What's_your_favorite_beach_activity": {
            "Sunbathing_nude": 0,
            "Skinny_dipping": 0,
            "Cruising": 0,
            "Beach_sex": 0,
        },
        "What's_your_preferred_video_length": {
            "Short_clips_1_3_mins": 0,
            "Medium_5_10_mins": 0,
            "Long_15_mins": 0,
            "Full_scenes_30_mins": 0,
        },
        "How_often_do_you_use_X": {
            "Daily": 0,
            "A_few_times_a_week": 0,
            "Weekly": 0,
            "Less_often": 0,
        },
        "Where_do_you_prefer_to_watch_content": {
            "OnlyFans": 0,
            "JustForFans": 0,
            "Twitter_X": 0,
            "Tube_sites": 0,
        },
    }

    submissions = {
        "total": 0,
        "What_type_of_content_makes_you_cum_the_hardest": 0,
        "What_kind_of_public_fun_turns_you_on_the_most": 0,
        "What_aspect_of_throat_fucking_excites_you": 0,
        "What's_your_favorite_part_of_bareback_action": 0,
        "Where_do_you_prefer_to_see_cumshots": 0,
        "What_natural_setting_gets_you_most_excited": 0,
        "What_crowded_place_turns_you_on_the_most": 0,
        "Which_form_of_public_transport_excites_you_most": 0,
        "What's_your_favorite_beach_activity": 0,
        "What's_your_preferred_video_length": 0,
        "How_often_do_you_use_X": 0,
        "Where_do_you_prefer_to_watch_content": 0,
    }

    ref.child("questions").set(questions)
    ref.child("submissions").set(submissions)

    print("Firebase structure setup completed.")


if __name__ == "__main__":
    setup_structure()
