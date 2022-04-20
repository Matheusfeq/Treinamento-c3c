import java.util.Scanner;
import java.util.Dictionary;
import java.util.Hashtable;

public class Operacoes 
{
    public static void mediaSalario(Dictionary dict, Double salarios[], int habitantes)
    {
        Double soma = 0.0;
        for(int i = 0; i < habitantes; i++)
        {
            soma += salarios[i];
        }
        Double media = soma/habitantes;
        dict.put("Média Salário", media);
    }

    public static void mediaFilhos(Dictionary dict, int filhos[], int habitantes)
    {
        Double soma = 0.0;
        for(int i = 0; i < habitantes; i++)
        {
            soma += filhos[i];
        }
        Double media = soma/habitantes;
        dict.put("Média Filhos", media);
    }

    public static void maiorSalario(Dictionary dict, Double salarios[], int habitantes)
    {
        Double s1 = salarios[0];
        Double s2 = 0.0;
        for(int i = 1; i < habitantes; i++)
        {
            s2 = salarios[i];
            if(s2 > s1)
            {
                s1 = s2;
            }
        }
        dict.put("Maior Salário", s1);
    }

    public static void salarioMenorQue150(Dictionary dict, Double salarios[], int habitantes)
    {
        Double cont = 0.0;
        for(int i = 0; i < habitantes; i++)
        {
            if(salarios[i] < 150)
            {
                cont++;
            }
        }
        Double porcentagem = cont/habitantes;
        dict.put("Porcentagem", porcentagem*100 + "%");
    }
}
