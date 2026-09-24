import java.util.*;

/**
 * CollectionsDemo · 集合框架：List / Map / Set / 泛型
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java CollectionsDemo.java
 *
 * 对应教程：d2.md 第 7、8 章。
 * 验收目标（学习计划）：能解释 ArrayList vs LinkedList 的取舍。
 */
public class CollectionsDemo {

    public static void main(String[] args) {
        listDemo();
        mapDemo();
        setDemo();
        genericDemo();
    }

    /** List：有序可重复 */
    static void listDemo() {
        System.out.println("== 1. List ==");

        // ArrayList：底层动态数组 —— 随机访问快，中间插入/删除慢  <- 默认首选
        // LinkedList：底层双向链表 —— 随机访问慢，头尾插入/删除快
        List<String> langs = new ArrayList<>();
        langs.add("Java");
        langs.add("TypeScript");
        langs.add("SQL");
        langs.add(1, "Go");                        // 指定位置插入
        System.out.println("langs = " + langs);

        System.out.println("size = " + langs.size());                    // 长度
        System.out.println("get(0) = " + langs.get(0));                  // 取值（像 arr[0]）
        System.out.println("contains(SQL) = " + langs.contains("SQL"));  // 包含
        langs.set(0, "JAVA");                      // 替换
        langs.remove("Go");                        // 按值删除
        System.out.println("处理后 = " + langs);

        // 遍历
        for (String s : langs) {
            System.out.println("  - " + s);
        }

        // 排序 + 工具方法
        List<Integer> nums = new ArrayList<>(List.of(3, 1, 4, 1, 5));
        nums.sort(Comparator.naturalOrder());
        System.out.println("sorted = " + nums);
        System.out.println("max = " + Collections.max(nums) + ", min = " + Collections.min(nums));
    }

    /** Map：键值对 */
    static void mapDemo() {
        System.out.println("\n== 2. Map ==");

        Map<String, Integer> stock = new HashMap<>();
        stock.put("苹果", 10);
        stock.put("香蕉", 5);
        stock.put("橙子", 8);
        stock.put("苹果", 12);   // key 重复会覆盖 value

        System.out.println("get(苹果) = " + stock.get("苹果"));
        System.out.println("getOrDefault(西瓜) = " + stock.getOrDefault("西瓜", 0));
        System.out.println("containsKey(香蕉) = " + stock.containsKey("香蕉"));

        // 遍历：entrySet 最常用【TS 对照】Object.entries()
        for (Map.Entry<String, Integer> e : stock.entrySet()) {
            System.out.println("  " + e.getKey() + " => " + e.getValue());
        }

        // computeIfAbsent：不存在则初始化（常用链式写法）
        Map<String, List<String>> tags = new HashMap<>();
        tags.computeIfAbsent("水果", k -> new ArrayList<>()).add("苹果");
        tags.computeIfAbsent("水果", k -> new ArrayList<>()).add("香蕉");
        System.out.println("tags = " + tags);
    }

    /** Set：去重 */
    static void setDemo() {
        System.out.println("\n== 3. Set ==");

        Set<String> pages = new HashSet<>();
        pages.add("首页");
        pages.add("药品详情");
        pages.add("首页");   // 重复，加不进去
        System.out.println("HashSet = " + pages + "，size = " + pages.size());

        // LinkedHashSet：去重 + 保持插入顺序（去重场景的常用选择）
        Set<Integer> deduped = new LinkedHashSet<>(List.of(3, 1, 3, 2, 1));
        System.out.println("LinkedHashSet 去重 = " + deduped);

        // TreeSet：去重 + 自动排序
        Set<Integer> sorted = new TreeSet<>(List.of(90, 60, 80, 60));
        System.out.println("TreeSet 排序 = " + sorted);
    }

    /** 泛型：编译期类型检查 */
    static void genericDemo() {
        System.out.println("\n== 4. 泛型 ==");

        System.out.println("max(3, 7) = " + max(3, 7));
        System.out.println("max(\"a\", \"b\") = " + max("a", "b"));

        List<String> names = new ArrayList<>();
        names.add("小米");
        // names.add(123);   // <- 取消注释会「编译报错」：泛型在编译期拦住类型错误
        System.out.println("names = " + names);
    }

    /** 泛型方法：<T extends Comparable<T>> 表示「实现了可比较接口的任意类型」 */
    static <T extends Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) >= 0 ? a : b;
    }
}
