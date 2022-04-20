import java.util.Scanner;
import java.util.Dictionary;
import java.util.Hashtable;

public class Dicio
{
    public static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args)
    {
        Double salarios[] = new Double[5];
        int filhos[] = new int[5];
        Dictionary dict = new Hashtable();
        int habitantes = 0;
        for(int i = 0; i < salarios.length; i++)
        {
            System.out.println("Insira o salário da " + (i+1) + "a pessoa:");
            salarios[i] = sc.nextDouble();
            System.out.println("Insira o número de filhos da " + (i+1) + "a pessoa:");
            filhos[i] = sc.nextInt();
            habitantes++;
            if(salarios[i] < 0)
                break;
        }
        
        Operacoes.mediaFilhos(dict, filhos, habitantes);
        Operacoes.mediaSalario(dict, salarios, habitantes);
        Operacoes.maiorSalario(dict, salarios, habitantes);
        Operacoes.salarioMenorQue150(dict, salarios, habitantes);
        System.out.println(dict);
    }
}