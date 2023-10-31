class Solution{
public:
	void pushZerosToEnd(int arr[], int n) {
	    // code here
	      int count = 0;

   for(int i =0;i<n;i++){

       if(arr[i]!=0){

           arr[count] = arr[i];

           count++;

       }

   }

   for(int i =count;i<n;i++){

       arr[i] = 0;

   }
	}
};
