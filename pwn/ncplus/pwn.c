#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const char *flag1 = "flag{I_hate_you}";
const char *flag2 = "flag{not_know_this}";
const char *flag3 = "flag{a_little_close}";

int read_line(char *buf, int size)
{
    if (fgets(buf, size, stdin) == NULL)
    {
        return -1;
    }
    buf[strcspn(buf, "\n")] = 0;
    return strlen(buf);
}

void func()
{
    char buf[40];
    puts("告诉我你的心意吧: ");
    fflush(stdout);
    gets(buf);
    return;
}

void secret_shell()
{
    puts("\n恭喜你触发了后门！获得shell权限\n");
    fflush(stdout);
    // system("/bin/sh");
    execve("/bin/sh", NULL, NULL);
}

int main()
{
    char buffer[1024];
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    printf("Debug: secret_shell = %p\n", secret_shell);
    puts("恭喜你成功使用了nc连接，现在请你回答下面的问题吧!\n\n");

    // 问题1
    puts("1）你愿意加入网安协会吗?(Y/n) ");
    if (read_line(buffer, sizeof(buffer)) < 0)
        return 0;

    if (strlen(buffer) == 0 || (buffer[0] != 'Y' && buffer[0] != 'y'))
    {
        puts("我不喜欢你!\n");
        puts(flag1);
        puts("\n");
        return 0;
    }

    // 问题2
    puts("2）下面的ACG人物中，哪位角色对25届会长影响最大?\n\n"
         "\t\t1.千反田える\t2.北白川玉子\t3.北白川馅子\t4.四宫辉夜\n"
         "\t\t5.高木同学\t6.樱野玖璃梦\t7.椎名真白\t8.椎名真冬\n"
         "\t\t9.椎名真昼\t10.牧之原翔子\t11.樱岛麻衣\t12.梓川(花)枫\n"
         "\t\t13.伊井野弥子\t14.花坂结衣\t15.绚辻词\t16.鹰仓杏铃\n"
         "\t\t17.鹰仓杏璃\t18.玉树樱\t19.栗山未来\t20.新堂爱\n"
         "\t\t21.白咲花\t22.星野日向\t23.姬坂乃爱\t24.香风智乃\n"
         "\t\t25.保登心爱\t26.桐间纱路\t27.德丽莎\t28.高板穗乃果\n"
         "\t\t29.南小鸟\t30.园田海未\t31.矢泽妮可\t32.伊莉雅\n"
         "\t\t33.水濑名雪\t34.神尾观铃\t35.古河渚\t36.枣岭\n"
         "\t\t37.神北小毬\t38.神户小鸟\t39.中津静流\t40.星野梦美\n"
         "\t\t41.立华奏\t42.五更琉璃\t43.新垣绫乃\t44.泉此方\n"
         "\t\t45.逢坂大河\t46.雪之下雪乃\t47.由比滨结衣\t48.一色彩羽\n"
         "\t\t49.樱之宫莓香\t50.绫波丽\t51.可儿那由多\t52.伊蕾娜\n"
         "\t\t53.夏娜\t\t54.珈百璃\t55.天使真央\t56.伊地知虹夏\n"
         "\t\t57.千代田桃\t58.空银子\t59.御坂美琴\t60.佐天泪子\n"
         "\t\t61.初春饰利\t62.木之本樱\t63.大道寺知世\t64.惠飞须泽胡桃\n"
         "\t\t65.土间埋\t66.加藤惠\t67.佐仓千代\t68.小鸟游六花\n"
         "\t\t69.友利奈绪\t70.平泽唯\t71.南梦芽\t72.一歧日和\n"
         "\t\t73.和泉纱雾\t74.锦明日海\t75.在原七海\t76.皆原阳茉莉\n"
         "\t\t77.鹿岛理理\t78.凉宫春日\t79.高町奈叶\t80.间桐樱(远坂樱)\n"
         "\t\t81.春埼美空\t82.䌷 文德斯\t83.花小泉杏\t84.莲\n"
         "\t\t85.小路绫\t86.九条可怜\t87.大宫忍\t88.爱丽丝·卡塔雷特\n"
         "\t\t89.战场原黑仪\t90.千石抚子\t91.东仪白\t92.塞西莉亚(白圣女与黑牧师)\n"
         "\t\t93.琪安娜\t94.芽衣\t\t95.爱莉希雅\t96.格蕾修\n"
         "\t\t97.流萤\t\t98.锦木千束\t99.井上泷奈\t100.鸢一折纸\n\n"
         "#）请输入选项：");

    if (read_line(buffer, sizeof(buffer)) < 0)
        return 0;

    if (strcmp(buffer, "19") != 0)
    {
        puts("我不喜欢你!\n");
        puts(flag2);
        puts("\n");
        return 0;
    }

    // 问题3
    puts("\n3）你喜欢谁捏？: ");
    func();
    return 0;
}