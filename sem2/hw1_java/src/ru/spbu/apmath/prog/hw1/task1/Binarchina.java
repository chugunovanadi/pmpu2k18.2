package ru.spbu.apmath.prog.hw1.task1;

public class Binarchina {
    private int number;
    public Binarchina(int number){
        this.number = number;
    }

    public String toBinary(){
        if (number < 0)
            throw new ArithmeticException("Неверный ввод. Введите не отрицательное число");
        int cope = number;
        StringBuilder answer = new StringBuilder();
        while (cope > 0){
            if (cope%2 ==1){
                answer.insert(0,'1');
            }else{answer.insert(0,'0');}
            cope = cope / 2;
        }
        return answer.toString();
    }
}

