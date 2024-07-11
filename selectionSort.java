
public class selectionSort {
    public static void displayArray(int name []){
        for (int i =0; i<name.length; i++){
            System.out.print(name[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int scores[] = {4,2,1,3};
        for (int i=0; i<scores.length-1; i++){
            int smallest = i;
            for (int j = smallest+1; j<scores.length; j++){
                if (scores[smallest] > scores[j]){
                    smallest = j;
                }


            }
            int temp = scores[i];
                scores [i]= scores[smallest];
                scores[smallest] = temp;
        }
        displayArray(scores);

    }
    
}