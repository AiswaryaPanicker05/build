#include <stdio.h>
struct process {
       int pid;
       int arrival;
       int burst;
       int completetion;
       int turnaround;
       int waiting;
};
int main() {
    int n;
    printf("enter the number of process:");
    scanf("%d",&n);
    
    struct Process p[n];
    
    //input process details
    for (int i=0; i < n; i++){
        for(int j=0;j< n-i-1;j++){
            if (p[j].arrival > p[j+1].arrival) {
                struct Process temp = p[j];
                p[j]=p[j+1]
                p[j+1]=temp
           }
        }
     }
     int current    Tim=0
     double totalwaiting = 0 
     //calculate ct tat wt
     for(int i=0;i<n;i++) {
        if (currentTime < p[i].arrival)
           currentTime = p[i].arrival;
           
         currentTime += p[i].burst;
         p[i].completion=currentTime;
         p[i].turnaround = p[i].completion-p[i].arrival;
         p[i].waiting = p[i].turnaround - p[i].burst;
         totalwaiting += p[i].waiting;
       }
       printf("/n fcfs sheduling:/n")
       printf("PID\t AT \t BT \t CT \t TAT \t TWT \n")
       for (int i=0;i<n;i++)  {
           printf("P %d/t %d/t %d/t %d/t %d/t %d/t/n")
                 p[i].pid,p[i].arrival,p[i].burst,
                 p[i].completion,p[i].turnaround,p[i].waiting):
       }
       printf("/n Average Waiting Time = %.2f/n",totalwaiting / n);
        return 0;
    }
