package com.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        Scanner scanner = new Scanner(System.in);

        // Pedir los datos al usuario por consola
        System.out.print("Ingrese el primer numero: ");
        double a = scanner.nextDouble();

        System.out.print("Ingrese el segundo numero: ");
        double b = scanner.nextDouble();

        // Realizar los calculos usando la instancia de Calculadora
        double resultadoSuma = calculadora.suma(a, b);
        double resultadoResta = calculadora.resta(a, b);
        double resultadoMultiplicacion = calculadora.multiplicacion(a, b);
        double resultadoDivision = calculadora.division(a, b);

        // Mostrar los resultados
        System.out.println("\n--- RESULTADOS ---");
        System.out.println("El resultado de la suma es: " + resultadoSuma);
        System.out.println("El resultado de la resta es: " + resultadoResta);
        System.out.println("El resultado de la multiplicacion es: " + resultadoMultiplicacion);
        
        // Validacion para evitar division por cero
        if (b != 0) {
            System.out.println("El resultado de la division es: " + resultadoDivision);
        } else {
            System.out.println("El resultado de la division es: No se puede dividir entre cero.");
        }

        scanner.close();
    }
}