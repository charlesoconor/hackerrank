import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static int init(){
        Scanner sc = new Scanner(System.in); 
        int temp = sc.nextInt();
        H = sc.nextInt();
        if ( temp < 0 || H < 0 ){
            throw Exception("Breadth and height must be positive");
        }
        return temp;
    }
    static int B = init();
    static int H;
    static boolean flag = true;

    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }

    }//end of main

}//end of class

