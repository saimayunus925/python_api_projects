
import requests # this is for handling API requests

def generate_random_activity():
    # generate a random activity
    activity_json = requests.get('http://www.boredapi.com/api/activity/').json()
    print(f'The activity: {activity_json["activity"]}!')
    print(f'What kind of activity is this? {activity_json["type"].upper()}')
    print(f'# of participants? {activity_json["participants"]}')
    if (activity_json['link'] == ""):
        print("Sorry! No link is available for the activity. We hope the other info is enough to help you get started!")
    else:
        print(f'Link? Here you go! {activity_json["link"]}')

if __name__ == '__main__':
    generate_random_activity()