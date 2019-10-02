import java.util.*;
import java.io.*;

class insertion{

    public void InsertionSort(int[]A){

        for(int i=1;i<A.length;i++)
        {
            int key= A[i];
            int j=i-1;
        while(j>=0 && key<A[j])
        {
            A[j+1]=A[j];
            j--;
        }
       
            A[j+1]=key;
            
        }
            
            }

public static void main(String[] args)throws Exception
{

    Scanner sc=new Scanner(System.in);

    System.out.println("Enter no. of inputs");
    int length =sc.nextInt();

    int[] A=new int[length];

    System.out.println();
    for(int i=0;i<length;i++)
    {
        A[i]=sc.nextInt();
    }
	
	insertion r1=new insertion();	

	r1.InsertionSort(A);

    System.out.println();

		for(int k=0;k<length;k++)
		{
		System.out.println(A[k]);
		}
			
}

}
