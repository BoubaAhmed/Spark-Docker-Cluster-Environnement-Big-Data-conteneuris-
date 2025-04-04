package com.Bouba;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.SparkConf;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class App {
    public static void main(String[] args) {

        SparkConf conf = new SparkConf()
                .setAppName("BoubaSumApp")
                .setMaster("spark://spark-master:7077");

        try (JavaSparkContext sc = new JavaSparkContext(conf)) {

            List<Integer> numbers = IntStream.rangeClosed(1, 100)
                    .boxed()
                    .collect(Collectors.toList());
            JavaRDD<Integer> rdd = sc.parallelize(numbers);

            int sum = rdd.reduce((a, b) -> a + b);

            System.out.println("La somme des entiers de 1 à 100 est : " + sum);
        }
    }
}
