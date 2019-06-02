import java.util.*;
//Knapsack problem yields maximum profit if profit:weight ratio is considered
class GreedyArray{
	int weight;
	int profit;
	Double pwratio;
	public GreedyArray(int weight,int profit){
		this.weight = weight;
		this.profit = profit;
		this.pwratio = (double)this.profit/this.weight;
	}
}

class GreedyKnapsack{
   static GreedyArray[] pwarr;
   static double findMaxProfit(int max_weight){
   	  double profit=0;
   	  int i=0;
   	  for(i =0;i<pwarr.length;i++){
   	  	if(max_weight>0 && pwarr[i].weight<=max_weight){
   	  		max_weight-=pwarr[i].weight;
            profit+=pwarr[i].profit;
   	  	}
   	  	else break;
   	  }
   	  //Taking fractional weight when complete weight can't be taken
   	  if(max_weight>0) profit+=(pwarr[i].profit*((double)max_weight/pwarr[i].weight));
   	  return profit;
   }
   public static void main(String[] args){
        int[] profits ={10,5,15,7,6,18,3};
        int[] weights ={2,3,5,7,1,4,1};
        int max_weight=15;
        pwarr = new GreedyArray[profits.length];
        for(int i=0;i<profits.length;i++)
        	 pwarr[i] = new GreedyArray(weights[i],profits[i]);
        //sorting elements based on profit:weight ratio
        Arrays.sort(pwarr,new Comparator<GreedyArray>(){
        	public int compare(GreedyArray a1,GreedyArray a2){
        		return a2.pwratio.compareTo(a1.pwratio);
        	}
        });
       System.out.println(findMaxProfit(max_weight));
   }
}
