package ru.spbu.apmath.prog.hw2.task1;

import java.util.Scanner;

public class DiscountsMain {
    public static void main(String[] args) throws IllegalArgumentException,ArithmeticException {
        System.out.println("Введите скидку магазина");
        Scanner tally = new Scanner(System.in);
        int value;
        try { value = tally.nextInt(); }
        catch (Exception e){
            throw new IllegalArgumentException("Введите целое число");
        }
        Discounts saleReal = new Discounts(value);
        System.out.println("Реальная скидка " + saleReal.sale() + "%");
    }

}
