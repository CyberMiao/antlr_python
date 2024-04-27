# 抽象树数据结构


class TreeNode:
    def __init__(self, value, kind='Terminal'):
        """
        构造函数，确定节点的内容及类型
        :param value: 节点内容
        :param kind: 节点类型
        """
        self.children = []
        self.value = value
        self.kind = kind

    def add_child(self, child):
        """
        添加孩子节点
        :param child: 子树
        """
        self.children.append(child)

    def get_child(self, index):
        """
        返回指定索引的节点
        :param index: 索引
        :return: 指定索引的子树
        """
        return self.children[index]

    def save_tree_to_file(self, dir_name, filename='SyntaxOut'):
        """
        调用save_tree函数保存树到指定文件
        :param dir_name: 文件夹名称
        :param filename: 文件名称
        :return:
        """
        # 保存结构+信息
        with open(dir_name + '/' + filename + '.struct', 'w') as file:
            self.save_tree(file, 0, True)
        # 仅保存信息
        with open(dir_name + '/' + filename + '.txt', 'w') as file:
            self.save_tree(file, 0, False)

    def save_tree(self, file, depth, kind):
        """
        在文件中写入树内容或结构
        :param file: 文件IO
        :param depth: 当前节点的深度
        :param kind: 是否写入节点的类型
        :return:
        """
        file.write("  " * depth + ((self.kind + ': ') if kind else '') + self.value + "\n")
        for child in self.children:
            child.save_tree(file, depth + 1, kind)
