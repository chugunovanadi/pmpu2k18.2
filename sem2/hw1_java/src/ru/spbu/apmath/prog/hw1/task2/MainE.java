package ru.spbu.apmath.prog.hw1.task2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MainE { public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println("Количество работников");
    int number_staff = in.nextInt();
    List<Employee> staff = new ArrayList<>();

    for(int i = 0;i<number_staff;i++){
        System.out.println("Имя работника");
        String WORKER_NAME = in.next();
        System.out.println("Зарплата в час");
        double MONEY_HOUR = in.nextDouble();
        System.out.println("Количество часов");
        int TIMER = in.nextInt();
        staff.add(new Employee(WORKER_NAME,MONEY_HOUR,TIMER));
    }

    for(Employee employee:staff){
        try{
            System.out.println(employee.getWORKER_NAME() + " " + employee.getMONEY_HOUR() + " " +
                    employee.getTIMER() +  " " + employee.getSalary());

        }catch (IllegalStateException e){
            System.out.println(employee.getWORKER_NAME() + " " + employee.getMONEY_HOUR() + " "
                    + employee.getTIMER() +  " " + "Ошибка!");
        }

    }

}
}
