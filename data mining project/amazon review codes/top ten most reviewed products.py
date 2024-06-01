from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from heapq import heappush, heappop
class TopTenReviewedProducts(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, data):
        # Parse JSON data and emit product ID with count 1
        yield None, (data['asin'], 1)

    def reducer_init(self):
        # Initialize min heap to store top 10 products
        self.top_products = []

    def reducer(self, _, values):
        product_counts = {}
        for product, count in values:
            product_counts[product] = product_counts.get(product, 0) + count

        for product, count in product_counts.items():
            # Push product and review count onto the heap
            heappush(self.top_products, (count, product))

            # Keep only top 10 products
            if len(self.top_products) > 10:
                heappop(self.top_products)
    def reducer_final(self):
        # Yield top ten reviewed products
        for count, product in sorted(self.top_products, reverse=True):
            yield product, count

if __name__ == '__main__':
    TopTenReviewedProducts.run()
