from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def setup_logging():
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )

def main():
    setup_logging()
    
    # Configuration Spark
    sc = SparkContext(appName="RealTimeSquareCalculator")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, batchDuration=1)  # Micro-batch de 1 seconde

    # Flux d'entrée
    lines = ssc.socketTextStream("producer", 9999)
    
    # Traitement
    numbers = lines.map(lambda x: int(x))
    squares = numbers.map(lambda n: (n, n**2))
    
    # Affichage des résultats
    squares.pprint(num=10)
    
    # Démarrage
    ssc.start()
    print("🎯 Consommateur prêt à traiter les données...")
    ssc.awaitTermination()

if __name__ == "__main__":
    main()