package ru.spbu.apmath.prog.hw2.task1;

public class Discounts {
    private int number;
    public Discounts(int number){
        this.number = number;
    }

    public int sale(){
        int copy = number;
        if (copy < 0)
            throw new ArithmeticException("Число должно быть не отрицательным");

        if (copy % 10 == copy){
            return copy;
        }
        int result = 0;
        while (copy != 0){
            result += copy % 10;
            copy /= 10;
        }
        number = result;
        return sale();
    }

}
