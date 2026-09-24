import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * TsUtilsDemo · 练习：用 Java 重写 10 个你熟悉的 TS 工具函数
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java TsUtilsDemo.java
 *
 * 对应教程：d2.md 第 14 章 & 学习计划 S1 实践任务。
 * 目标：感受「同一件事」在两种语言里的表达差异，形成肌肉记忆。
 */
public class TsUtilsDemo {

    public static void main(String[] args) {
        System.out.println("1. unique     " + unique(List.of(1, 2, 2, 3, 3, 3)));              // [1, 2, 3]
        System.out.println("2. chunk      " + chunk(List.of(1, 2, 3, 4, 5), 2));               // [[1, 2], [3, 4], [5]]
        System.out.println("3. groupBy    " + groupBy(List.of("apple", "avocado", "banana"), w -> w.charAt(0)));
        System.out.println("4. sum        " + sum(List.of(1, 2, 3, 4)));                        // 10
        System.out.println("5. max        " + max(List.of(3, 9, 2)));                           // Optional[9]
        System.out.println("6. reverse    " + reverse("hello"));                               // olleh
        System.out.println("7. palindrome " + isPalindrome("A man, a plan, a canal: Panama")); // true
        System.out.println("8. capitalize " + capitalize("java"));                             // Java
        System.out.println("9. flatten    " + flatten(List.of(List.of(1, 2), List.of(3))));     // [1, 2, 3]
        System.out.println("10. wordCount " + wordCount(List.of("a", "b", "a", "c", "a")));     // {a=3, b=1, c=1}
    }

    /** 1. 数组去重    TS: [...new Set(arr)] */
    static <T> List<T> unique(List<T> list) {
        return new ArrayList<>(new LinkedHashSet<>(list));   // 去重 + 保留原顺序
    }

    /** 2. 分块        TS: 手写 slice 循环 */
    static <T> List<List<T>> chunk(List<T> list, int size) {
        List<List<T>> result = new ArrayList<>();
        for (int i = 0; i < list.size(); i += size) {
            result.add(new ArrayList<>(list.subList(i, Math.min(i + size, list.size()))));
        }
        return result;
    }

    /** 3. 按规则分组  TS: reduce 手写 */
    static <K, V> Map<K, List<V>> groupBy(List<V> list, Function<V, K> keyFn) {
        Map<K, List<V>> map = new HashMap<>();
        for (V v : list) {
            map.computeIfAbsent(keyFn.apply(v), k -> new ArrayList<>()).add(v);
        }
        return map;
    }

    /** 4. 求和        TS: arr.reduce((acc, x) => acc + x, 0) */
    static int sum(List<Integer> nums) {
        return nums.stream().mapToInt(Integer::intValue).sum();
    }

    /** 5. 最大值      TS: Math.max(...arr) */
    static Optional<Integer> max(List<Integer> nums) {
        return nums.stream().max(Integer::compareTo);
    }

    /** 6. 反转字符串  TS: [...s].reverse().join("") */
    static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }

    /** 7. 回文判断    TS: 清洗后与反转比较 */
    static boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return cleaned.equals(reverse(cleaned));
    }

    /** 8. 首字母大写  TS: s[0].toUpperCase() + s.slice(1) */
    static String capitalize(String s) {
        if (s == null || s.isEmpty()) {
            return s;
        }
        return Character.toUpperCase(s.charAt(0)) + s.substring(1);
    }

    /** 9. 拍平一层    TS: arr.flat() */
    static <T> List<T> flatten(List<List<T>> nested) {
        return nested.stream().flatMap(List::stream).collect(Collectors.toList());
    }

    /** 10. 词频统计   TS: reduce 手写 */
    static Map<String, Long> wordCount(List<String> words) {
        return words.stream().collect(Collectors.groupingBy(w -> w, Collectors.counting()));
    }
}

/*
 * 扩展练习（对应学习计划）：
 * 1. 再实现 5 个常用函数：range(start, end)、repeat(str, n)、
 *    compact(过滤 null)、intersection(交集)、shuffle(难度高，可跳过)；
 * 2. 把 groupBy 升级成支持「值转换」的版本（像 lodash 的 groupBy + mapValues 组合）。
 */
