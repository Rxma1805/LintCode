描述  
给一个 01 矩阵，求不同的岛屿的个数。  
0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。  
样例  
样例 1：  
输入：  
[  
  [1,1,0,0,0],  
  [0,1,0,0,1],  
  [0,0,0,1,1],  
  [0,0,0,0,0],  
  [0,0,0,0,1]  
]  
输出：  
3  
样例 2： 
  
输入：  
[  
  [1,1]  
]  
输出：  
1  
  
[解题思路：](https://blog.csdn.net/yurenguowang/article/details/77483402)  
1）逐个遍历  
2）检测到1就把 它重置为0  
3）然后递归与其相邻的四个位置，检测到1就置为0  
