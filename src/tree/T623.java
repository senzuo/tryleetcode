package tree;

/**
 * 没有考虑到 d==1 root 不为空特殊情况
 */
public class T623 {
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        if (d == 1 ){
            if (root == null)
                return new TreeNode(v);
            else{
                TreeNode t = new TreeNode(v);
                t.left = root;
                return t;
            }
        }
        if (d == 2) {
            TreeNode left = new TreeNode(v);
            TreeNode right = new TreeNode(v);
            left.left = root.left;
            right.right = root.right;
            root.right = right;
            root.left = left;
        } else {
            if (root.left != null)
                root.left = addOneRow(root.left, v, d - 1);
            if (root.right != null)
                root.right = addOneRow(root.right, v, d - 1);
        }
        return root;
    }
}
