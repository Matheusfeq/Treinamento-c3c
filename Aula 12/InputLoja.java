import java.util.Scanner;
public class InputLoja 
{
    public static Scanner sc = new Scanner(System.in);
    
    public static String obterNome()
    {
        System.out.println("Digite o nome da mercadoria: ");
        String nome = sc.next();
        return nome;
    }

    public static Integer obterQuantidadeMinima()
    {
        System.out.println("Digite a quantidade mínima da mercadoria: ");
        int minimo;
        while(true)
        {
            minimo = sc.nextInt();
            if(minimo <= 0)
            {
                System.out.println("Quantidade inválida! Tente novamente:");
            }
            else
            {
                break;
            }
        }
        return minimo;
    }

    public static Integer obterQuantidadeMaxima()
    {
        System.out.println("Digite a quantidade máxima da mercadoria: ");
        int maximo;
        while(true)
        {
            maximo = sc.nextInt();
            if(maximo <= 0)
            {
                System.out.println("Quantidade inválida! Tente novamente:");
            }
            else
            {
                break;
            }
        }
        return maximo;
    }

    public static Integer obterQuantidadeAtual(Object maximo)
    {
        System.out.println("Digite a quantidade atual da mercadoria: ");
        int atual;
        while(true)
        {
            atual = sc.nextInt();
            if(atual > (int)maximo || atual < 0)
            {
                System.out.println("Quantidade inválida! Tente novamente:");
            }
            else
            {
                break;
            }
        }
        return atual;
    }

    public static double obterValorUnitario()
    {
        System.out.println("Digite o valor unitário da mercadoria: ");
        Double valor;
        while(true)
        {
            valor = sc.nextDouble();
            if(valor <= 0)
            {
                System.out.println("Valor inválido! Tente novamente:");
            }
            else
            {
                break;
            }
        }
        return valor;
    }
}
