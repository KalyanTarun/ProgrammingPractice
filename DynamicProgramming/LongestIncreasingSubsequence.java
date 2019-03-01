import java.util.*;
class LIS{
	static void LongestIncreasingSubsequence(int[] a){
	ArrayList<ArrayList<Integer>> lis=new ArrayList<>(a.length);
    int ms=1,mi=0;
    //Initializing lists into list of lists
    for(int i=0;i<a.length;i++){
    	lis.add(new ArrayList<Integer>());
    }
    //lis = [[], [], [], [], [], []]

    //Adding the first element to list
    lis.get(0).add(a[0]); //lis= [[3], [], [], [], [], []]

    //System.out.println(lis);
    for(int i=1;i<a.length;i++){
    	for(int j=0;j<i;j++){
    		if((a[j]<a[i]) && (lis.get(i).size()< lis.get(j).size()+1)){
    		   
               //The following code is synonymous to lis[i]=lis[j]
               
               ArrayList<Integer> al=new ArrayList<>(lis.get(j)); 			
               lis.add(i,al);
               lis.remove(i+1);
    			
    		}
    	}
    	lis.get(i).add(a[i]);

        //Finding the max size obtained till now and max size index
    	if(lis.get(i).size()>ms){
	    	ms=lis.get(i).size();
	    	mi=i;
	    }
	}
    	System.out.println(lis.get(mi));
    }
    

	public static void main(String[] args){
		int[] a=new int[]{3,2,6,4,5,1};
		LongestIncreasingSubsequence(a);
	}
}
