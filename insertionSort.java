/**
 * imsertionSort
 */
public class insertionSort {
    public static void displayArray(int name []){
        for (int i =0; i<name.length; i++){
            System.out.print(name[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int marks [] = {5,4,3,2,1};
        for (int i =1; i<marks.length; i++){
            int current = marks[i];
            int j = i-1;
            while(j>=0 && current <  marks[j]){
                marks[j+1] = marks[j];
                j--;
            }

            //placement 
            marks[j+1] = current;
        }
        displayArray(marks);
    }
    
}