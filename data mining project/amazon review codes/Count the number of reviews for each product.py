from mrjob.job import MRJob
import json


class ReviewCount(MRJob):

    def mapper(self, _, line):
        # Parse the JSON data
        data = json.loads(line)

        # Emit product ID as key and 1 as value for each review
        yield data['asin'], 1

    def reducer(self, key, values):
        # Sum up the count of reviews for each product
        total_reviews = sum(values)

        # Emit product ID and total reviews
        yield key, total_reviews


if __name__ == '__main__':
    ReviewCount.run()