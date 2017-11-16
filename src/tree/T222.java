package tree;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 统计完全二叉树的节点数
 * <p>
 * 满二叉树
 * 高度为 h =>  2^(h+1) - 1  enough!
 * shit! complete tree
 */


public class T222 {

    /**
     * : Time Limit Exceeded More Details
     *
     * @param root
     * @return
     */
    public int countNodes0(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        int count = 0;
        q.add(root);
        while (!q.isEmpty()) {
            root = q.poll();
            count++;
            if (root.left != null) q.add(root.left);
            if (root.right != null) q.add(root.right);
        }
        return count;
    }

    /**
     * : Time Limit Exceeded More Details
     *
     * @param root
     * @return
     */
    public int countNodes00(TreeNode root) {
        if (root != null) return countNodes00(root.left) + countNodes00(root.right) + 1;
        else return 0;
    }

    int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }

    public int countNodes(TreeNode root) {
        int h = height(root);
        if (h < 0) return 0;

        // 左右子树同样高
        if (height(root.right) == h - 1) {
            return 1 << h + countNodes(root.right);
        } else {
            return 1 << (h - 1) + countNodes(root.left);
        }
    }

//    public int countNodes1(TreeNode root) {
//        int h = height(root);
//        return h < 0 ? 0 :
//                height(root.right) == h - 1 ? (1 << h) + countNodes(root.right)
//                        : (1 << h - 1) + countNodes(root.left);
//    }
}
