import java.util.Arrays;

/**
 * SyntaxBasicsDemo · 基础语法演示：变量与类型 / 字符串 / 数组 / 流程控制
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java SyntaxBasicsDemo.java
 *
 * 对应教程：d2.md 第 1~5 章。【TS 对照】= 给你的前端经验对照点。
 */
public class SyntaxBasicsDemo {

    public static void main(String[] args) {
        types();
        strings();
        arrays();
        controlFlow();
    }

    /** 1. 变量与基本类型 */
    static void types() {
        System.out.println("== 1. 变量与类型 ==");

        // 【TS 对照】TS 只有 number；Java 把数字细分为多种类型
        int age = 25;                        // 最常用的整数
        long population = 8_100_000_000L;    // 超大整数要加 L；下划线只是方便阅读
        double price = 19.9;                 // 最常用的小数
        float rate = 0.85f;                  // float 少用，字面量要加 f
        boolean vip = true;                  // 布尔
        char grade = 'A';                    // 单个字符：单引号
        String name = "小明";                 // 字符串是「引用类型」：双引号

        // var：让编译器推断类型（Java 10+，只能用于局部变量）【TS 对照】let x = ...
        var city = "杭州";
        var score = 95;

        // final = 常量【TS 对照】const
        final double PI = 3.14159;

        System.out.println("name=" + name + ", city=" + city + ", score=" + score);
        System.out.println("grade=" + grade + ", vip=" + vip + ", rate=" + rate);
        System.out.println("PI=" + PI + ", price=" + price + ", population=" + population);

        // 类型转换：小范围 -> 大范围自动；反方向要强制转换（可能损失精度）
        long big = age;              // int -> long 自动
        int narrowed = (int) big;    // long -> int 强制
        System.out.println("big=" + big + ", narrowed=" + narrowed);
    }

    /** 2. 字符串 */
    static void strings() {
        System.out.println("\n== 2. 字符串 ==");

        String s = "Hello, Java World";

        // 【TS 对照】length 是方法（要带括号）；TS 是属性 s.length
        System.out.println("length()        = " + s.length());
        System.out.println("substring(7,11) = " + s.substring(7, 11)); // 左闭右开，像 slice
        System.out.println("indexOf(Java)   = " + s.indexOf("Java"));
        System.out.println("replace         = " + s.replace("World", "Agent"));
        System.out.println("contains(Java)  = " + s.contains("Java"));   // 像 includes
        System.out.println("toUpperCase     = " + s.toUpperCase());

        // 拆分与拼接
        String[] parts = "a,b,c".split(",");
        System.out.println("split           = " + Arrays.toString(parts)); // 数组要借 Arrays.toString 打印
        System.out.println("join            = " + String.join(" | ", parts));

        // 拼接：少量用 +，格式化用 String.format
        System.out.println("拼接            = " + ("你好，" + "小明"));
        System.out.println("格式化          = " + String.format("我是%s，今年%d岁", "小明", 25));

        // 文本块（Java 15+）：多行字符串
        String report = """
                项目：AI 健康管家
                阶段：S1 · Java 基础
                """;
        System.out.println("文本块:");
        System.out.print(report);

        // ★ 高频考点：字符串比较用 equals，== 比的是引用地址！
        String a = new String("abc");
        String b = new String("abc");
        System.out.println("a == b          -> " + (a == b));        // false
        System.out.println("a.equals(b)     -> " + a.equals(b));     // true
    }

    /** 3. 数组 */
    static void arrays() {
        System.out.println("\n== 3. 数组 ==");

        int[] preset = { 3, 1, 4, 1, 5 };   // 字面量初始化（定长）
        int[] zeros = new int[5];           // 默认全 0

        // 【TS 对照】长度是属性 .length（注意：字符串的 length 是方法）
        System.out.println("preset.length = " + preset.length + ", zeros[0] = " + zeros[0]);

        // 增强 for【TS 对照】for (const n of preset)
        int sum = 0;
        for (int n : preset) {
            sum += n;
        }
        System.out.println("sum = " + sum);

        // Arrays 工具类
        Arrays.sort(preset);
        System.out.println("sorted = " + Arrays.toString(preset));
        int[] first3 = Arrays.copyOf(preset, 3);
        System.out.println("copyOf(3) = " + Arrays.toString(first3));
        System.out.println("binarySearch(4) = " + Arrays.binarySearch(preset, 4));

        // 定长数组不够灵活 -> ArrayList（见 CollectionsDemo）
    }

    /** 4. 流程控制 */
    static void controlFlow() {
        System.out.println("\n== 4. 流程控制 ==");

        int score = 85;

        // if / else：与 TS 完全一致
        String level;
        if (score >= 90) {
            level = "A";
        } else if (score >= 60) {
            level = "B";
        } else {
            level = "C";
        }
        System.out.println("level = " + level);

        // switch 传统写法：每个 case 要 break，否则「穿透」
        switch (level) {
            case "A":
                System.out.println("评价：优秀");
                break;
            case "B":
                System.out.println("评价：及格");
                break;
            default:
                System.out.println("评价：加油");
        }

        // switch 表达式 + 箭头（Java 14+）：不需要 break，能直接赋值
        int day = 3;
        String dayType = switch (day) {
            case 1, 2, 3, 4, 5 -> "工作日";
            case 6, 7 -> "周末";
            default -> "非法日期";
        };
        System.out.println("dayType = " + dayType);

        // for / while / do-while：与 TS 一致
        int total = 0;
        for (int i = 1; i <= 100; i++) {
            total += i;
        }
        System.out.println("1+2+...+100 = " + total);

        // break / continue：与 TS 一致
        StringBuilder odd = new StringBuilder();
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue;  // 跳过偶数
            if (i > 7) break;          // 大于 7 结束
            odd.append(i).append(" ");
        }
        System.out.println("奇数(<=7): " + odd.toString().trim());
    }
}
