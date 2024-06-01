from mrjob.job import MRJob
import json
class AverageHelpfulness(MRJob):

    def mapper(self, _, line):
        # Parse the JSON data
        data = json.loads(line)
        # Extract helpful and total votes
        vote = data.get('vote', '0')  # Default to '0' if vote is missing
        # Remove commas and convert vote to an integer
        vote = int(vote.replace(',', '')) if ',' in vote else int(vote)
        # Emit product ID as key and helpful votes and total votes as value
        yield data['asin'], (vote, vote)
    def reducer(self, key, values):
        # Initialize variables to aggregate helpful and total votes
        total_helpful = 0
        total_votes = 0
        # Iterate through values and aggregate helpful and total votes
        for helpful, total in values:
            total_helpful += helpful
            total_votes += total
        # Calculate the average helpfulness score
        if total_votes > 0:
            average_helpfulness = total_helpful / total_votes
        else:
            average_helpfulness = 0
        # Yield product ID and average helpfulness score
        yield key, average_helpfulness
if __name__ == '__main__':
    AverageHelpfulness.run()
