/**
 * OopDemo · 面向对象演示：类 / 封装 / 继承 / 多态 / 抽象类 / 接口 / record
 *
 * 运行方式（JDK 11+ 单文件直接运行）：
 *   java OopDemo.java
 *
 * 对应教程：d2.md 第 6 章。
 */
public class OopDemo {

    public static void main(String[] args) {
        // ---------- 1. 类与对象 ----------
        System.out.println("== 1. 类与对象 ==");
        Dog wangcai = new Dog("旺财", 3);
        Cat mimi = new Cat("咪咪", 2);
        System.out.println(wangcai);   // 调用重写后的 toString()
        wangcai.say();
        mimi.say();

        // 封装：外部只能通过 getter/setter 访问 private 字段
        wangcai.setName("旺财二世");
        System.out.println("改名后: " + wangcai.getName());

        // ---------- 2. 多态 ----------
        System.out.println("\n== 2. 多态：父类引用指向子类对象 ==");
        Animal[] animals = { wangcai, mimi, new Dog("大黄", 5) };
        for (Animal a : animals) {
            a.say();   // 运行时动态绑定到各自的实现
        }

        // ---------- 3. 接口 ----------
        System.out.println("\n== 3. 接口：定义「能做什么」==");
        Swimmable[] swimmers = { wangcai, new Duck("唐老鸭") };
        for (Swimmable s : swimmers) {
            s.swim();
        }

        // ---------- 4. record：一行数据类 ----------
        System.out.println("\n== 4. record（不可变数据类）==");
        Point p = new Point(3, 4);
        System.out.println("p = " + p);                         // 自动生成 toString
        System.out.println("p.x() = " + p.x());                 // 访问器是 x() 不是 getX()
        Point p2 = new Point(3, 4);
        System.out.println("p.equals(p2) = " + p.equals(p2));   // 自动生成 equals -> true

        // ---------- 5. static：属于类，不属于对象 ----------
        System.out.println("\n== 5. static 成员 ==");
        new Counter();
        new Counter();
        new Counter();
        System.out.println("创建了 " + Counter.count + " 个 Counter 对象（count 是 static，全类共享）");
    }
}

// ==================== 类定义区域 ====================

/** 抽象类：不能 new，只能被继承；定义「共同的属性与行为」 */
abstract class Animal {
    private String name;    // private：仅本类可访问
    protected int age;      // protected：子类也可访问

    public Animal(String name, int age) {
        this.name = name;   // this 区分「字段」与「参数」
        this.age = age;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    /** 抽象方法：子类必须实现 */
    public abstract void say();

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" + name + ", " + age + "岁)";
    }
}

/** 接口：只有行为约定，实现类必须提供实现 */
interface Swimmable {
    void swim();
}

class Dog extends Animal implements Swimmable {
    public Dog(String name, int age) {
        super(name, age);   // 必须先调用父类构造器
    }

    @Override
    public void say() {
        System.out.println(getName() + "：汪汪汪！");
    }

    @Override
    public void swim() {
        System.out.println(getName() + "：狗刨式游泳～");
    }
}

class Cat extends Animal {
    public Cat(String name, int age) { super(name, age); }

    @Override
    public void say() {
        System.out.println(getName() + "：喵～");
    }
}

class Duck extends Animal implements Swimmable {
    public Duck(String name) { super(name, 1); }

    @Override
    public void say() { System.out.println(getName() + "：嘎嘎嘎"); }

    @Override
    public void swim() { System.out.println(getName() + "：在池塘里优雅地游"); }
}

/** record：不可变数据类（Java 16+） */
record Point(int x, int y) { }

/** static 演示：count 属于类本身，所有对象共享一份 */
class Counter {
    static int count = 0;

    Counter() {
        count++;   // 每 new 一次 +1
    }
}

/*
 * 扩展练习：
 * 1. 加一个 Pig 类（extends Animal），say() 输出「哼哼」；
 * 2. 让 Pig 也实现 Swimmable（猪也会游泳！）；
 * 3. 把它加进 main 的多态数组里，再跑一遍看输出。
 */
