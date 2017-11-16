package tree;

import java.util.LinkedList;
import java.util.Queue;

/**
 *  problem : 找出二叉树最底层最左边的值
 *  基本思路:
 *          最底层:按层遍历二叉树
 *                  使用队列非递归遍历
 *          最左边:
 *                  先遍历右边后左边即可
 */

public class T513 {
    public static void main(String[] args) {

    }
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        TreeNode treeNode = null;
        while (!queue.isEmpty()){
            treeNode = queue.poll();
            if (treeNode.right!=null)   queue.add(treeNode.right);
            if (treeNode.left!=null)    queue.add(treeNode.left);
        }
        return treeNode.val;
    }
}
