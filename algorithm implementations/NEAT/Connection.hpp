#ifndef CONNECTION_HPP
#define CONNECTION_HPP

class Connection
{

private:

    bool    enabled;
    double  weight;
    Node*   in_node;
    Node*   out_node;
    int     innov;

public:

    Connection();
    ~Connection();

    double update();

};

#endif
