package ru.spbu.apmath.prog.hw1.task1;

public class Binarchina {
    private int number;
    public Binarchina(int number){
        this.number = number;
    }

    public String toBinary(){
        StringBuilder answer = new StringBuilder();
        while (number > 0){
            if (number%2 ==1){
                answer.insert(0,'1');
            }else{answer.insert(0,'0');}
            number = number / 2;
        }
        return answer.toString();
    }
}

