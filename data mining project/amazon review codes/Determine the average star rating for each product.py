from mrjob.job import MRJob
import json


class AverageStarRating(MRJob):

    def mapper(self, _, line):
        # Parse the JSON data
        data = json.loads(line)

        # Emit product ID as key and star rating as value
        yield data['asin'], data['overall']

    def reducer(self, key, values):
        total_ratings = 0
        count = 0
        # Calculate sum of ratings and count of ratings for each product
        for rating in values:
            total_ratings += rating
            count += 1
        # Calculate average star rating with four decimal places
        average_rating = round(total_ratings / count, 4) if count > 0 else 0

        # Emit product ID and average star rating
        yield key, average_rating

if __name__ == '__main__':
    AverageStarRating.run()
