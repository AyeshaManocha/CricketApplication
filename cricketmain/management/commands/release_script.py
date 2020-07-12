from django.core.management.base import BaseCommand, CommandError
from cricketmain.management.commands import update_create
from cricketmain.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):

        update_create.update_create(Team,{"name":"Team one","logo_uri":'https://static.toiimg.com/photo/msid-66933404/66933404.jpg?resizemode=4&width=400',"club_state":"Delhi"},{"name":"Team one","logo_uri":'https://static.toiimg.com/photo/msid-66933404/66933404.jpg?resizemode=4&width=400',"club_state":"Delhi"},{})
        update_create.update_create(Team,{"name":"Team two","logo_uri":'https://png.pngitem.com/pimgs/s/573-5732445_mumbai-indians-logo-mumbai-indians-logo-png-transparent.png',"club_state":"Mumbai"},{"name":"Team two","logo_uri":'https://png.pngitem.com/pimgs/s/573-5732445_mumbai-indians-logo-mumbai-indians-logo-png-transparent.png',"club_state":"Mumbai"},{})
        update_create.update_create(Team,{"name":"Team three","logo_uri":'https://www.pngkit.com/png/detail/269-2695213_kkr-squad-ipl-kolkata-knight-riders-logo-png.png',"club_state":"Kolkata"},{"name":"Team three","logo_uri":'https://www.pngkit.com/png/detail/269-2695213_kkr-squad-ipl-kolkata-knight-riders-logo-png.png',"club_state":"Kolkata"},{})
        update_create.update_create(Team,{"name":"Team four","logo_uri":'https://www.kindpng.com/picc/m/489-4898659_royal-challengers-bangalore-rcb-logo-royal-challengers-bangalore.png',"club_state":"Bengaluru"},{"name":"Team four","logo_uri":'https://www.kindpng.com/picc/m/489-4898659_royal-challengers-bangalore-rcb-logo-royal-challengers-bangalore.png',"club_state":"Bengaluru"},{})

        teamone = Team.objects.get(name="Team one")
        teamtwo = Team.objects.get(name="Team two")
        teamthree = Team.objects.get(name="Team three")
        teamfour = Team.objects.get(name="Team four")

        update_create.update_create(Player,{"first_name":"Virat","last_name":"Kohli", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/The_President%2C_Shri_Pranab_Mukherjee_presenting_the_Padma_Shri_Award_to_Shri_Virat_Kohli%2C_at_a_Civil_Investiture_Ceremony%2C_at_Rashtrapati_Bhavan%2C_in_New_Delhi_on_March_30%2C_2017_%28cropped%29.jpg/260px-thumbnail.jpg',"jersey_number":1,"country": "India","history":"Batsman","team_id": teamone.id},
        {"first_name":"Virat","last_name":"Kohli", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/The_President%2C_Shri_Pranab_Mukherjee_presenting_the_Padma_Shri_Award_to_Shri_Virat_Kohli%2C_at_a_Civil_Investiture_Ceremony%2C_at_Rashtrapati_Bhavan%2C_in_New_Delhi_on_March_30%2C_2017_%28cropped%29.jpg/260px-thumbnail.jpg',"jersey_number":1,"country": "India","history":"Batsman","team_id": teamone.id},{})
        update_create.update_create(Player,{"first_name":"MS","last_name":"Dhoni", "image_uri":'https://imagevars.gulfnews.com/2019/07/20/MS-Dhoni_16c0e955558_large.jpg',"jersey_number":7,"country": "India","history":"Wicket keeper","team_id": teamone.id},
        {"first_name":"MS","last_name":"Dhoni", "image_uri":'https://imagevars.gulfnews.com/2019/07/20/MS-Dhoni_16c0e955558_large.jpg',"jersey_number":7,"country": "India","history":"Batsman","team_id": teamone.id},{})
        update_create.update_create(Player,{"first_name":"Rohit","last_name":"Sharma", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Rohit_Sharma_November_2016_%28cropped%29.jpg/260px-Rohit_Sharma_November_2016_%28cropped%29.jpg',"jersey_number":17,"country": "India","history":"Batsman","team_id": teamone.id},
        {"first_name":"Rohit","last_name":"Sharma", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Rohit_Sharma_November_2016_%28cropped%29.jpg/260px-Rohit_Sharma_November_2016_%28cropped%29.jpg',"jersey_number":17,"country": "India","history":"Batsman","team_id": teamone.id},{})

        update_create.update_create(Player,{"first_name":"Hardik","last_name":"Pandya", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/5/5b/Hardik_Pandya_%28cropped%29.jpg',"jersey_number": 21,"country": "India","history":"All rounder","team_id": teamtwo.id},
        {"first_name":"Hardik","last_name":"Pandya", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/5/5b/Hardik_Pandya_%28cropped%29.jpg',"jersey_number": 21,"country": "India","history":"All rounder","team_id": teamtwo.id},{})
        update_create.update_create(Player,{"first_name":"Ravindra","last_name":"Jadeja", "image_uri":'https://www.cricbuzz.com/stats/img/faceImages/587.jpg',"jersey_number":27,"country": "India","history":"All rounder","team_id": teamtwo.id},
        {"first_name":"Ravindra","last_name":"Jadeja", "image_uri":'https://www.cricbuzz.com/stats/img/faceImages/587.jpg',"jersey_number":27,"country": "India","history":"All rounder","team_id": teamtwo.id},{})
        update_create.update_create(Player,{"first_name":"Jasprit","last_name":"Bumrah", "image_uri":'https://m.cricbuzz.com/a/img/v1/192x192/i1/c170685/jasprit-bumrah.jpg',"jersey_number":37,"country": "India","history":"Bowler","team_id": teamtwo.id},
        {"first_name":"Jasprit","last_name":"Bumrah", "image_uri":'https://m.cricbuzz.com/a/img/v1/192x192/i1/c170685/jasprit-bumrah.jpg',"jersey_number":37,"country": "India","history":"Bowler","team_id": teamtwo.id},{})

        update_create.update_create(Player,{"first_name":"Rishabh","last_name":"Pant", "image_uri":'https://pbs.twimg.com/profile_images/1255017319635410944/lFsXKEs_.jpg',"jersey_number": 5,"country": "India","history":"Wicket-keeper","team_id": teamthree.id},
        {"first_name":"Rishabh","last_name":"Pant", "image_uri":'https://pbs.twimg.com/profile_images/1255017319635410944/lFsXKEs_.jpg',"jersey_number": 5,"country": "India","history":"Wicket-keeper","team_id": teamthree.id},{})
        update_create.update_create(Player,{"first_name":"Bhuvneshwar","last_name":"Kumar", "image_uri":'https://m.cricbuzz.com/a/img/v1/192x192/i1/c170689/bhuvneshwar-kumar.jpg',"jersey_number":56,"country": "India","history":"Bowler","team_id": teamthree.id},
        {"first_name":"Bhuvneshwar","last_name":"Kumar", "image_uri":'https://m.cricbuzz.com/a/img/v1/192x192/i1/c170689/bhuvneshwar-kumar.jpg',"jersey_number":56,"country": "India","history":"Bowler","team_id": teamthree.id},{})
        update_create.update_create(Player,{"first_name":"Kuldeep","last_name":"Yadav", "image_uri":'https://www.cricket.com.au/-/media/Players/Men/International/India/ODIWC19/Kuldeep-Yadav-CWC19.ashx',"jersey_number":39,"country": "India","history":"Bowler","team_id": teamthree.id},
        {"first_name":"Kuldeep","last_name":"Yadav", "image_uri":'https://www.cricket.com.au/-/media/Players/Men/International/India/ODIWC19/Kuldeep-Yadav-CWC19.ashx',"jersey_number":39,"country": "India","history":"Bowler","team_id": teamthree.id},{})

        update_create.update_create(Player,{"first_name":"Dinesh","last_name":"Karthik", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/f/fc/Dinesh.Karthik.jpg',"jersey_number": 12,"country": "India","history":"Wicket-keeper","team_id": teamfour.id},
        {"first_name":"Dinesh","last_name":"Karthik", "image_uri":'https://upload.wikimedia.org/wikipedia/commons/f/fc/Dinesh.Karthik.jpg',"jersey_number": 12,"country": "India","history":"Wicket-keeper","team_id": teamfour.id},{})
        update_create.update_create(Player,{"first_name":"Mohammed","last_name":"Shami", "image_uri":'https://www.cricket.com.au/-/media/Players/Men/International/India/ODIWC19/Mohammed-Shami-CWC19.ashx',"jersey_number":24,"country": "India","history":"Bowler","team_id": teamfour.id},
        {"first_name":"Mohammed","last_name":"Shami", "image_uri":'https://www.cricket.com.au/-/media/Players/Men/International/India/ODIWC19/Mohammed-Shami-CWC19.ashx',"jersey_number":24,"country": "India","history":"Bowler","team_id": teamfour.id},{})
        update_create.update_create(Player,{"first_name":"Yuzvendra","last_name":"Chahal", "image_uri":'https://timesofindia.indiatimes.com/thumb/msid-73356504,width-1200,height-900,resizemode-4/.jpg',"jersey_number":28,"country": "India","history":"Bowler","team_id": teamfour.id},
        {"first_name":"Yuzvendra","last_name":"Chahal", "image_uri":'https://timesofindia.indiatimes.com/thumb/msid-73356504,width-1200,height-900,resizemode-4/.jpg',"jersey_number":28,"country": "India","history":"Bowler","team_id": teamfour.id},{})
        



