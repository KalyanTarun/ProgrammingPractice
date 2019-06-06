import java.util.*;
class ShoppingQueue{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int paths = sc.nextInt();
		sc.nextLine();
		String num ="";
		String na[] = new String[2];
		HashMap<Integer,StringBuilder> hm = new HashMap<>();
		for(int i =0;i<paths-1;i++){
			num = sc.nextLine();
			//System.out.println(num);
            na = num.split(" ");
			if(hm.get(na[0]) == null)
            	hm.put(Integer.parseInt(na[0]),new StringBuilder(na[1]));
            else 
              	hm.put(Integer.parseInt(na[0]),hm.get(Integer.parseInt(na[0])).append(na[1]));
            if(hm.get(na[1]) == null)
            	hm.put(Integer.parseInt(na[1]),new StringBuilder(na[0]));
            else 
              	hm.put(Integer.parseInt(na[1]),hm.get(Integer.parseInt(na[1])).append(na[0]));
		}
		System.out.println(hm);
	}
}