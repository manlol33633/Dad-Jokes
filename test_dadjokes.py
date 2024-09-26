import unittest
import subprocess
import urllib.request
import json
import time


class Test(unittest.TestCase):

    def setUp(self):
        print('Spinning up server')
        self.child = subprocess.Popen(args=['python', 'dadjokes.py'], stdout=None)
        time.sleep(2)   ## Time to come up

    def tearDown(self):
        print('Killing server')
        try: 
            self.child.terminate()
            self.child.kill()
        except:
            print('Error terminating server child process')

    def test_home(self):
        req = urllib.request.Request('http://localhost:3001')
        response = urllib.request.urlopen(req)
        try:
            data = json.loads(response.read())
        except:
            self.fail('Could not parse JSON on home page request')

        self.assertEqual(200, response.getcode(),
                         'Home page request did not return a 200 status header')
        self.assertEqual(
            {'success': True, 'message': 'This is the home page'}, data, 'Home page response incorrect')

    def test_404(self):
        req = urllib.request.Request('http://localhost:3001/something-invalid')
        try:
            response = urllib.request.urlopen(req)

            # Shouldn't get here because urlopen should throw exception
            self.fail('Invalid route did not return the correct status header')
        except urllib.error.HTTPError as e:
            self.assertEqual(404, e.code,
                             'Invalid route did not return a 404 status header')


    def test_random(self):
        runs = []
        for x in range(20):

            req = urllib.request.Request('http://localhost:3001/random')
            try:
                response = urllib.request.urlopen(req)
                data = json.loads(response.read())
            except urllib.error.HTTPError as e:
                self.fail('Invalid response from random request')

            if not data['id'] in runs:
                runs.append(data['id'])

        if len(runs) < 18:
            self.fail('Random route returned too many duplicates')

    def test_jokes(self):
        tests = [{
            "id": "74bddcfd",
            "name": "Nut Assault",
            "joke": "Two peanuts were walking down the street. One was a salted."
        },
            {
            "id": "0009b5e4",
            "name": "Golfer Pants",
            "joke": "Why did the golfer bring two pairs of pants? In case he got a hole-in-one."
        },
            {
            "id": "90482c63",
            "name": "Lieutenant Dan",
            "joke": "To the man in the wheelchair that stole my camouflage jacket; You can hide, but you can't run."
        },
            {
            "id": "3a6276ef",
            "name": "My Day",
            "joke": "The rotation of earth really makes my day."
        },
            {
            "id": "fa4617bb",
            "name": "Chickens can't drive",
            "joke": "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans."
        },
            {
            "id": "fa5eeda3",
            "name": "Bel Air",
            "joke": "How do you find Will Smith in the snow? You look for the fresh prints."
        },
            {
            "id": "ab0be3ec",
            "name": "I'm Positive",
            "joke": "Two atoms are walking down the street. One says, \"Oh no! I lost an electron!\", The other asks him, \"Are you sure?\", The first one says, \"Yeah, I'm positive\""
        },
            {
            "id": "64e2fc14",
            "name": "Sandwich",
            "joke": "A ham sandwich walks into a bar and orders a beer. The bartender looks at him and says, \"Sorry we don't serve food here.\""
        },
            {
            "id": "18c42b79",
            "name": "I Can't Hear This Joke",
            "joke": "What is Beethoven's favorite fruit? A ba-na-na-na."
        },
            {
            "id": "db4c6a4a",
            "name": "Watch Your Head",
            "joke": "Two guys walk into a bar, the third one ducks."
        },
            {
            "id": "03ac5ebb",
            "name": "Every 6 Months",
            "joke": "What time did the man go to the dentist? Tooth hurt-y."
        }]

        for test in tests:
            req = urllib.request.Request(
                'http://localhost:3001/joke?id=' + test['id'])
            try:
                response = urllib.request.urlopen(req)
            except:
                self.fail('Error requesting url for /joke?id=' + test['id'])
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on joke page request')
            self.assertEqual(200, response.getcode(),
                             'Home page request did not return a 200 status header')
            self.assertEqual(test['id'], data['id'], 'Incorrect id returned')
            self.assertEqual(test['name'], data['name'],
                             'Incorrect name returned for joke ' + test['id'])
            self.assertEqual(
                test['joke'], data['joke'], 'Incorrect joke returned for id ' + test['id'])


    def test_bad_jokes(self):
        tests = ['hello', 'this', 'is', 'an', 'invalid', 'joke']
        for test in tests:
            req = urllib.request.Request(
                'http://localhost:3001/joke?id=' + test)
            try:
                response = urllib.request.urlopen(req)

                # Shouldn't get here because urlopen should throw exception
                self.fail(
                    'Invalid route did not return the correct status header')
            except urllib.error.HTTPError as e:
                self.assertEqual(404, e.code,
                                 'Invalid route did not return a 404 status header')


if __name__ == '__main__':
    unittest.main()