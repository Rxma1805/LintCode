Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).  

样例  
Example 1:  

Input：{1,2,3}  
Output：[[1],[2,3]]  
Explanation：  
  1  
 / \  
2   3  
it will be serialized {1,2,3}  
level order traversal  
Example 2:  
  
Input：{1,#,2,3}  
Output：[[1],[2],[3]]  
Explanation：   
1  
 \  
  2  
 /  
3  
it will be serialized {1,#,2,3}  
level order traversal  
挑战  
Challenge 1: Using only 1 queue to implement it.  
  
Challenge 2: Use BFS algorithm to do it.  

注意事项  
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.  
The number of nodes does not exceed 20.  
[解题思路](https://blog.csdn.net/yurenguowang/article/details/76906620)
1）把Root节点放在队列里面  
2）弹出Root，压入他下面的孩子节点，并且记录长度  
3）for  range(length)   循环弹出队列的节点，并把孩子节点压入
4）完成一层，把tmp队列 添加到结果里面
