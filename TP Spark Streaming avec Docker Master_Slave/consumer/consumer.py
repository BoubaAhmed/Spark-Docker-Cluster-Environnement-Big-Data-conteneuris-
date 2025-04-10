from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def process_stream():
    setup_logging()
    
    sc = SparkContext(appName="RealTimeSquareCalculator")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, batchDuration=1)
    
    lines = ssc.socketTextStream("producer", 9999)
    
    numbers = lines.map(lambda x: int(x.strip()))
    squares = numbers.map(lambda n: (n, n**2))
    
    squares.pprint(num=10)
    
    ssc.start()
    print("🎯 Consumer ready to process data...")
    ssc.awaitTermination()

if __name__ == "__main__":
    process_stream()