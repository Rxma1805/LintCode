597. 具有最大平均数的子树
描述
中文
English
给一棵二叉树，找到有最大平均值的子树。返回子树的根结点。

LintCode会打印出根结点为你返回节点的子树，保证有最大平均数子树只有一棵

您在真实的面试中是否遇到过这个题？  
样例
样例1

输入：
{1,-5,11,1,2,4,-2}
输出：11
说明:
这棵树如下所示：
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
11子树的平均值是4.333，为最大的。
样例2

输入：
{1,-5,11}
输出：11
说明:
     1
   /   \
 -5     11
1,-5,11 三棵子树的平均值分别是 2.333,-5,11。因此11才是最大的  

# 返回和以及数目  

