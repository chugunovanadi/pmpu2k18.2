package ru.spbu.apmath.prog.hw1.task1;

import java.util.Scanner;

public class MainB {
    public static void main(String[] args) throws IllegalArgumentException,ArithmeticException {
        System.out.println("Введите число");
        Scanner tally = new Scanner(System.in);
        int num;
        try {
            num = tally.nextInt();
        }catch (Exception e){
            throw new IllegalArgumentException("Неверный ввод. Введите число");
        }

        if (num < 0){
            throw new ArithmeticException("Неверный ввод. Введите не отрицательное число");
        }

        Binarchina result = new Binarchina(num);
        System.out.println("В двоичной системе:" + result.toBinary());
    }
}

