from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Tony Stark', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='captain@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='superman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='Yoga', duration=20, calories=100)

        # Create workouts
        cardio = Workout.objects.create(name='Cardio', description='Cardio workout')
        strength = Workout.objects.create(name='Strength', description='Strength workout')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
