900. 二叉搜索树中最接近的值  
 
给一棵非空二叉搜索树以及一个target值，找到在BST中最接近给定值的节点值  

样例  
Example1  

Input: root = {5,4,9,2,#,8,10} and target = 6.124780  
Output: 5  
Explanation：  
Binary tree {5,4,9,2,#,8,10},  denote the following structure:  
        5  
       / \  
     4    9  
    /    / \  
   2    8  10  
Example2  
  
Input: root = {3,2,4,1} and target = 4.142857  
Output: 4  
Explanation：  
Binary tree {3,2,4,1},  denote the following structure :  
     3  
    / \  
  2    4  
 /  
1  
注意事项  
给出的目标值为浮点数  
我们可以保证只有唯一一个最接近给定值的节点  
